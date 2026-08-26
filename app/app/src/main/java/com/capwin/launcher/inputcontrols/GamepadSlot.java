package com.capwin.launcher.inputcontrols;

public interface GamepadSlot {
    String getName();

    short getVendorId();

    short getProductId();

    GamepadState getGamepadState();

    GamepadVibration getGamepadVibration();
}
