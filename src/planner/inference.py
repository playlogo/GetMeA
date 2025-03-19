import requests
import json

from config import config

from typing import TypedDict

from planner.collector import get_linux_flavor


# Types
class MessageType(TypedDict):
    role: str
    content: str


class FirstJudgeResType(TypedDict):
    name: str
    description: str
    bestSource: str
    packageInstallCMD: str


class BasePrompt:
    model = config.getConfig()["models"]["planner"]

    def inference(
        self, messages: list[MessageType], double_json=False, reasoning=False
    ):
        req = requests.post(
            f"{config.getConfig()["openai"]["base_url"]}/chat/completions",
            json={
                "model": self.model,
                "messages": messages,
                "response_format": {"type": "json_object"} if double_json else None,
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {config.getConfig()["openai"]['token']}",
            },
        )

        if req.status_code != 200:
            # Request failed
            # TODO: Retry 2 - 3 times
            raise Exception(f"Inference failed with model {self.model}: {req.text}")

        res = req.json()

        if double_json:
            return json.loads(res["choices"][0]["message"]["content"])
        else:
            return res["choices"][0]["message"]["content"]


class FirstJudge(BasePrompt):
    model = config.getConfig()["models"]["planner"]

    def run(self, program: str) -> FirstJudgeResType:
        # Get linux flavor
        flavor = get_linux_flavor()

        res = self.inference(
            [
                {
                    "role": "system",
                    "content": f"""You are a Linux system administration expert! The user will provide the name of a software, library, or program available on Linux.

Your task is to determine whether the software is available in the standard system package registry (such as dnf, apk, etc.) or if the user needs to install it manually by browsing the web (e.g., Bun, NVM [Node Version Manager]).
- Only state that the software is in the package registry if you are ABSOLUTLY certain it is available.
- If you are unsure, ALWAYS DEFAULT to web research as the preferred installation method.

For context, the system is running the following Linux distribution:
{flavor} 

Please respond only in the following JSON format (without a code block, just raw JSON):
{{
  "name": "<software name>",
  "description": "<short description of the software>",
  "bestSource": "PackageRegistry" | "WebResearch",
  "packageInstallCMD": "<command to install on the given linux distro if in package registry, always add a -y flag or similar for automatic installation>"
}}""",
                },
                {"role": "user", "content": program},
            ],
            double_json=True,
            reasoning=True,
        )

        return res
