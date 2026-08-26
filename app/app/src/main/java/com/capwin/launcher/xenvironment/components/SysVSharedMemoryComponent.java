package com.capwin.launcher.xenvironment.components;

import com.capwin.launcher.sysvshm.SysVSHMConnectionHandler;
import com.capwin.launcher.sysvshm.SysVSHMRequestHandler;
import com.capwin.launcher.sysvshm.SysVSharedMemory;
import com.capwin.launcher.xconnector.UnixSocketConfig;
import com.capwin.launcher.xconnector.XConnectorEpoll;
import com.capwin.launcher.xenvironment.EnvironmentComponent;
import com.capwin.launcher.xserver.SHMSegmentManager;
import com.capwin.launcher.xserver.XServer;

public class SysVSharedMemoryComponent extends EnvironmentComponent {
    private XConnectorEpoll connector;
    public final UnixSocketConfig socketConfig;
    private SysVSharedMemory sysVSharedMemory;
    private final XServer xServer;

    public SysVSharedMemoryComponent(XServer xServer, UnixSocketConfig socketConfig) {
        this.xServer = xServer;
        this.socketConfig = socketConfig;
    }

    @Override
    public void start() {
        if (connector != null) return;
        sysVSharedMemory = new SysVSharedMemory();
        connector = new XConnectorEpoll(socketConfig, new SysVSHMConnectionHandler(sysVSharedMemory), new SysVSHMRequestHandler());
        connector.start();

        xServer.setSHMSegmentManager(new SHMSegmentManager(sysVSharedMemory));
    }

    @Override
    public void stop() {
        if (connector != null) {
            connector.destroy();
            connector = null;
        }

        sysVSharedMemory.deleteAll();
    }
}
