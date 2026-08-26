# CapWin Launcher — Native fork build guide

## Mục đích

CapWin Launcher là fork kỹ thuật của Winlator để quản lý container Windows x86_64 cho workflow thử nghiệm CapCut trên Android ARM64. Fork này không chứa CapCut, installer, codec hoặc DLL sở hữu độc quyền. Người dùng tự cung cấp phần mềm Windows mà họ có quyền sử dụng.

## Toolchain đã được source pin

| Thành phần | Giá trị trong source | Lý do cần khớp |
|---|---:|---|
| Android compile SDK | 35 | `app/build.gradle` dùng `compileSdk 35`. |
| Android NDK | 24.0.8215888 | C++/JNI build trong `externalNativeBuild`. |
| CMake | 3.22.1 | Được Gradle cấu hình cho các native renderer. |
| Gradle Wrapper | 8.14.5 | Được khai báo tại `gradle/wrapper/gradle-wrapper.properties`. |
| ABI | arm64-v8a | Fork hiện lọc build về ARM64; phù hợp Redmi Turbo 3. |

## Chuẩn bị máy build

Cài Android Studio, Android SDK Platform 35, Android NDK `24.0.8215888`, CMake `3.22.1`, JDK tương thích Android Gradle Plugin và Git. Clone phải luôn có submodule:

```bash
git clone --recurse-submodules <URL_FORK_CAPWIN>
cd capwin-launcher/app
./gradlew assembleDebug
```

Nếu môi trường Android Studio chưa tự nhận NDK/CMake, vào **SDK Manager → SDK Tools** để cài đúng phiên bản được pin ở trên. Chỉ thực hiện build sau khi kiểm tra đầy đủ license/attribution và sau khi review thay đổi source.

## Trình tự smoke test

1. Cài APK debug lên Redmi Turbo 3 rồi mở một lần để runtime giải nén và tạo container.
2. Tạo container mặc định, chọn profile Turnip/DXVK và bật log Wine/Box64.
3. Chạy một chương trình Windows x86_64 nhỏ đã được phép sử dụng để kiểm tra cửa sổ, cảm ứng/mouse, âm thanh, filesystem và log.
4. Chỉ sau khi smoke test ổn định mới import một bản CapCut Windows do người dùng tự tải và cấp quyền sử dụng.
5. Lưu log và profile riêng cho CapCut; không dùng profile “đạt” của app nhẹ để suy ra CapCut sẽ chạy ổn định.

> Build thành công không đồng nghĩa CapCut tương thích. Các lỗi renderer, codec, .NET, filesystem hoặc CPU translation phải được phân tích bằng log trên đúng thiết bị.
