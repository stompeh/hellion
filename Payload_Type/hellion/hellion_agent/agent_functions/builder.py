from mythic_container.PayloadBuilder import *
from mythic_container.MythicCommandBase import *
from mythic_container.MythicRPC import *
import json

class Apfell(PayloadType):
    name = "hellion"
    file_extension = "bin"
    author = "stompeh"
    supported_os = [SupportedOS.Windows, SupportedOS.Linux]
    wrapper = False
    wrapped_payloads = []
    note = """General purpose payload for Windows and Linux"""
    supports_dynamic_loading = True
    c2_profiles = ["http"]
    mythic_encrypts = True
    translation_container = "hellion_trans" # "myPythonTranslation"
    build_parameters = []
    agent_path = pathlib.Path(".") / "hellion"
    agent_icon_path = agent_path / "hellion.svg"
    agent_code_path = agent_path / "agent_code"

    build_steps = [
        BuildStep(step_name="Gathering Files", step_description="Making sure all commands have backing files on disk"),
        BuildStep(step_name="Configuring", step_description="Stamping in configuration values")
    ]

    async def build(self) -> BuildResponse:
        # this function gets called to create an instance of your payload
        resp = BuildResponse(status=BuildStatus.Success)
        return resp