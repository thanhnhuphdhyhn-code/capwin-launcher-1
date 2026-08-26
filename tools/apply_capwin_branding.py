from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ANDROID = ROOT / "app"
SOURCE_ICON = Path("/home/ubuntu/capwin-launcher/assets/images/icon.png")


def replace_in_file(path: Path, replacements: dict[str, str]) -> None:
    content = path.read_text(encoding="utf-8")
    updated = content
    for original, replacement in replacements.items():
        updated = updated.replace(original, replacement)
    if updated != content:
        path.write_text(updated, encoding="utf-8")


def update_package_references() -> None:
    for path in ANDROID.rglob("*"):
        if path.suffix not in {".java", ".xml", ".cpp", ".h", ".cmake", ".gradle", ".pro"}:
            continue
        replace_in_file(path, {"com.winlator": "com.capwin.launcher"})

    build_file = ANDROID / "app" / "build.gradle"
    replace_in_file(build_file, {"namespace 'com.winlator'": "namespace 'com.capwin.launcher'", "applicationId 'com.winlator'": "applicationId 'com.capwin.launcher'"})

    manifest = ANDROID / "app" / "src" / "main" / "AndroidManifest.xml"
    replace_in_file(
        manifest,
        {
            'android:appCategory="game"': 'android:appCategory="video"',
            'android:isGame="true"': 'android:isGame="false"',
        },
    )


def update_display_name() -> None:
    for path in (ANDROID / "app" / "src" / "main" / "res").glob("values*/strings.xml"):
        replace_in_file(path, {"<string name=\"app_name\">Winlator</string>": "<string name=\"app_name\">CapWin Launcher</string>"})


def update_runtime_labels() -> None:
    replacements = {
        "Project(Winlator)": "Project(CapWinRuntime)",
        "Software\\\\Winlator\\\\WFM": "Software\\\\CapWin\\\\WFM",
        '"Winlator/profiles/"': '"CapWin Launcher/profiles/"',
        '"Winlator"': '"CapWin Launcher"',
    }
    paths = [
        ANDROID / "app" / "src" / "main" / "cpp" / "winlator" / "CMakeLists.txt",
        ANDROID / "app" / "src" / "main" / "java" / "com" / "capwin" / "launcher" / "core" / "WineUtils.java",
        ANDROID / "app" / "src" / "main" / "java" / "com" / "capwin" / "launcher" / "inputcontrols" / "InputControlsManager.java",
        ANDROID / "app" / "src" / "main" / "java" / "com" / "capwin" / "launcher" / "widget" / "LogView.java",
        ANDROID / "app" / "src" / "main" / "java" / "com" / "capwin" / "launcher" / "xserver" / "extensions" / "GLXExtension.java",
    ]
    for path in paths:
        replace_in_file(path, replacements)


def update_icons() -> None:
    if not SOURCE_ICON.exists():
        raise FileNotFoundError(f"Không tìm thấy icon nguồn: {SOURCE_ICON}")

    sizes = {
        "mipmap-mdpi": 48,
        "mipmap-hdpi": 72,
        "mipmap-xhdpi": 96,
        "mipmap-xxhdpi": 144,
        "mipmap-xxxhdpi": 192,
    }
    with Image.open(SOURCE_ICON) as source:
        image = source.convert("RGBA")
        for folder, size in sizes.items():
            output = image.resize((size, size), Image.Resampling.LANCZOS)
            destination = ANDROID / "app" / "src" / "main" / "res" / folder
            for filename in ("ic_launcher.png", "ic_launcher_round.png", "ic_launcher_foreground.png"):
                output.save(destination / filename, format="PNG", optimize=True)


def main() -> None:
    update_package_references()
    update_display_name()
    update_runtime_labels()
    update_icons()
    print("CapWin branding applied")


if __name__ == "__main__":
    main()
