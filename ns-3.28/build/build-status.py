#! /usr/bin/env python

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.28-aodv-debug', 'build/src/bridge/examples/ns3.28-csma-bridge-debug', 'build/src/bridge/examples/ns3.28-csma-bridge-one-hop-debug', 'build/src/buildings/examples/ns3.28-buildings-pathloss-profiler-debug', 'build/src/config-store/examples/ns3.28-config-store-save-debug', 'build/src/core/examples/ns3.28-main-callback-debug', 'build/src/core/examples/ns3.28-sample-simulator-debug', 'build/src/core/examples/ns3.28-main-ptr-debug', 'build/src/core/examples/ns3.28-main-random-variable-debug', 'build/src/core/examples/ns3.28-main-random-variable-stream-debug', 'build/src/core/examples/ns3.28-sample-random-variable-debug', 'build/src/core/examples/ns3.28-sample-random-variable-stream-debug', 'build/src/core/examples/ns3.28-command-line-example-debug', 'build/src/core/examples/ns3.28-hash-example-debug', 'build/src/core/examples/ns3.28-sample-log-time-format-debug', 'build/src/core/examples/ns3.28-test-string-value-formatting-debug', 'build/src/core/examples/ns3.28-main-test-sync-debug', 'build/src/csma/examples/ns3.28-csma-one-subnet-debug', 'build/src/csma/examples/ns3.28-csma-broadcast-debug', 'build/src/csma/examples/ns3.28-csma-packet-socket-debug', 'build/src/csma/examples/ns3.28-csma-multicast-debug', 'build/src/csma/examples/ns3.28-csma-raw-ip-socket-debug', 'build/src/csma/examples/ns3.28-csma-ping-debug', 'build/src/csma-layout/examples/ns3.28-csma-star-debug', 'build/src/dsdv/examples/ns3.28-dsdv-manet-debug', 'build/src/dsr/examples/ns3.28-dsr-debug', 'build/src/energy/examples/ns3.28-li-ion-energy-source-debug', 'build/src/energy/examples/ns3.28-rv-battery-model-test-debug', 'build/src/energy/examples/ns3.28-basic-energy-model-test-debug', 'build/src/fd-net-device/examples/ns3.28-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.28-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.28-realtime-dummy-network-debug', 'build/src/fd-net-device/examples/ns3.28-realtime-fd2fd-onoff-debug', 'build/src/fd-net-device/examples/ns3.28-fd-emu-ping-debug', 'build/src/fd-net-device/examples/ns3.28-fd-emu-udp-echo-debug', 'build/src/fd-net-device/examples/ns3.28-fd-emu-onoff-debug', 'build/src/fd-net-device/examples/ns3.28-fd-tap-ping-debug', 'build/src/fd-net-device/examples/ns3.28-fd-tap-ping6-debug', 'build/src/internet/examples/ns3.28-main-simple-debug', 'build/src/internet-apps/examples/ns3.28-dhcp-example-debug', 'build/src/lr-wpan/examples/ns3.28-lr-wpan-packet-print-debug', 'build/src/lr-wpan/examples/ns3.28-lr-wpan-phy-test-debug', 'build/src/lr-wpan/examples/ns3.28-lr-wpan-data-debug', 'build/src/lr-wpan/examples/ns3.28-lr-wpan-error-model-plot-debug', 'build/src/lr-wpan/examples/ns3.28-lr-wpan-error-distance-plot-debug', 'build/src/lte/examples/ns3.28-lena-cqi-threshold-debug', 'build/src/lte/examples/ns3.28-lena-dual-stripe-debug', 'build/src/lte/examples/ns3.28-lena-fading-debug', 'build/src/lte/examples/ns3.28-lena-intercell-interference-debug', 'build/src/lte/examples/ns3.28-lena-ipv6-addr-conf-debug', 'build/src/lte/examples/ns3.28-lena-ipv6-ue-rh-debug', 'build/src/lte/examples/ns3.28-lena-ipv6-ue-ue-debug', 'build/src/lte/examples/ns3.28-lena-pathloss-traces-debug', 'build/src/lte/examples/ns3.28-lena-profiling-debug', 'build/src/lte/examples/ns3.28-lena-rem-debug', 'build/src/lte/examples/ns3.28-lena-rem-sector-antenna-debug', 'build/src/lte/examples/ns3.28-lena-rlc-traces-debug', 'build/src/lte/examples/ns3.28-lena-simple-debug', 'build/src/lte/examples/ns3.28-lena-simple-epc-debug', 'build/src/lte/examples/ns3.28-lena-deactivate-bearer-debug', 'build/src/lte/examples/ns3.28-lena-x2-handover-debug', 'build/src/lte/examples/ns3.28-lena-x2-handover-measures-debug', 'build/src/lte/examples/ns3.28-lena-frequency-reuse-debug', 'build/src/lte/examples/ns3.28-lena-distributed-ffr-debug', 'build/src/lte/examples/ns3.28-lena-uplink-power-control-debug', 'build/src/lte/examples/ns3.28-lena-simple-epc-emu-debug', 'build/src/mesh/examples/ns3.28-mesh-debug', 'build/src/mobility/examples/ns3.28-main-grid-topology-debug', 'build/src/mobility/examples/ns3.28-main-random-topology-debug', 'build/src/mobility/examples/ns3.28-main-random-walk-debug', 'build/src/mobility/examples/ns3.28-mobility-trace-example-debug', 'build/src/mobility/examples/ns3.28-ns2-mobility-trace-debug', 'build/src/mobility/examples/ns3.28-bonnmotion-ns2-example-debug', 'build/src/mpi/examples/ns3.28-simple-distributed-debug', 'build/src/mpi/examples/ns3.28-third-distributed-debug', 'build/src/mpi/examples/ns3.28-nms-p2p-nix-distributed-debug', 'build/src/mpi/examples/ns3.28-simple-distributed-empty-node-debug', 'build/src/netanim/examples/ns3.28-dumbbell-animation-debug', 'build/src/netanim/examples/ns3.28-grid-animation-debug', 'build/src/netanim/examples/ns3.28-star-animation-debug', 'build/src/netanim/examples/ns3.28-wireless-animation-debug', 'build/src/netanim/examples/ns3.28-uan-animation-debug', 'build/src/netanim/examples/ns3.28-colors-link-description-debug', 'build/src/netanim/examples/ns3.28-resources-counters-debug', 'build/src/network/examples/ns3.28-main-packet-header-debug', 'build/src/network/examples/ns3.28-main-packet-tag-debug', 'build/src/network/examples/ns3.28-packet-socket-apps-debug', 'build/src/nix-vector-routing/examples/ns3.28-nix-simple-debug', 'build/src/nix-vector-routing/examples/ns3.28-nms-p2p-nix-debug', 'build/src/ns3-rmcat/examples/ns3.28-gcc-example-debug', 'build/src/olsr/examples/ns3.28-simple-point-to-point-olsr-debug', 'build/src/olsr/examples/ns3.28-olsr-hna-debug', 'build/src/point-to-point/examples/ns3.28-main-attribute-value-debug', 'build/src/propagation/examples/ns3.28-main-propagation-loss-debug', 'build/src/propagation/examples/ns3.28-jakes-propagation-model-example-debug', 'build/src/sixlowpan/examples/ns3.28-example-sixlowpan-debug', 'build/src/sixlowpan/examples/ns3.28-example-ping-lr-wpan-debug', 'build/src/spectrum/examples/ns3.28-adhoc-aloha-ideal-phy-debug', 'build/src/spectrum/examples/ns3.28-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-debug', 'build/src/spectrum/examples/ns3.28-adhoc-aloha-ideal-phy-with-microwave-oven-debug', 'build/src/spectrum/examples/ns3.28-tv-trans-example-debug', 'build/src/spectrum/examples/ns3.28-tv-trans-regional-example-debug', 'build/src/stats/examples/ns3.28-gnuplot-example-debug', 'build/src/stats/examples/ns3.28-double-probe-example-debug', 'build/src/stats/examples/ns3.28-time-probe-example-debug', 'build/src/stats/examples/ns3.28-gnuplot-aggregator-example-debug', 'build/src/stats/examples/ns3.28-gnuplot-helper-example-debug', 'build/src/stats/examples/ns3.28-file-aggregator-example-debug', 'build/src/stats/examples/ns3.28-file-helper-example-debug', 'build/src/tap-bridge/examples/ns3.28-tap-csma-debug', 'build/src/tap-bridge/examples/ns3.28-tap-csma-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.28-tap-wifi-virtual-machine-debug', 'build/src/tap-bridge/examples/ns3.28-tap-wifi-dumbbell-debug', 'build/src/topology-read/examples/ns3.28-topology-example-sim-debug', 'build/src/traffic-control/examples/ns3.28-red-tests-debug', 'build/src/traffic-control/examples/ns3.28-red-vs-ared-debug', 'build/src/traffic-control/examples/ns3.28-adaptive-red-tests-debug', 'build/src/traffic-control/examples/ns3.28-pfifo-vs-red-debug', 'build/src/traffic-control/examples/ns3.28-codel-vs-pfifo-basic-test-debug', 'build/src/traffic-control/examples/ns3.28-codel-vs-pfifo-asymmetric-debug', 'build/src/traffic-control/examples/ns3.28-pie-example-debug', 'build/src/uan/examples/ns3.28-uan-cw-example-debug', 'build/src/uan/examples/ns3.28-uan-rc-example-debug', 'build/src/uan/examples/ns3.28-uan-raw-example-debug', 'build/src/uan/examples/ns3.28-uan-ipv4-example-debug', 'build/src/uan/examples/ns3.28-uan-ipv6-example-debug', 'build/src/uan/examples/ns3.28-uan-6lowpan-example-debug', 'build/src/virtual-net-device/examples/ns3.28-virtual-net-device-debug', 'build/src/wave/examples/ns3.28-wave-simple-80211p-debug', 'build/src/wave/examples/ns3.28-wave-simple-device-debug', 'build/src/wave/examples/ns3.28-vanet-routing-compare-debug', 'build/src/wifi/examples/ns3.28-wifi-phy-test-debug', 'build/src/wifi/examples/ns3.28-test-interference-helper-debug', 'build/src/wifi/examples/ns3.28-wifi-manager-example-debug', 'build/src/wifi/examples/ns3.28-wifi-trans-example-debug', 'build/src/wimax/examples/ns3.28-wimax-ipv4-debug', 'build/src/wimax/examples/ns3.28-wimax-multicast-debug', 'build/src/wimax/examples/ns3.28-wimax-simple-debug', 'build/examples/tcp/ns3.28-tcp-large-transfer-debug', 'build/examples/tcp/ns3.28-tcp-nsc-lfn-debug', 'build/examples/tcp/ns3.28-tcp-nsc-zoo-debug', 'build/examples/tcp/ns3.28-tcp-star-server-debug', 'build/examples/tcp/ns3.28-star-debug', 'build/examples/tcp/ns3.28-tcp-bulk-send-debug', 'build/examples/tcp/ns3.28-tcp-pcap-nanosec-example-debug', 'build/examples/tcp/ns3.28-tcp-nsc-comparison-debug', 'build/examples/tcp/ns3.28-tcp-variants-comparison-debug', 'build/examples/tcp/ns3.28-tcp-pacing-debug', 'build/examples/udp/ns3.28-udp-echo-debug', 'build/examples/realtime/ns3.28-realtime-udp-echo-debug', 'build/examples/naming/ns3.28-object-names-debug', 'build/examples/tutorial/ns3.28-hello-simulator-debug', 'build/examples/tutorial/ns3.28-first-debug', 'build/examples/tutorial/ns3.28-second-debug', 'build/examples/tutorial/ns3.28-third-debug', 'build/examples/tutorial/ns3.28-fourth-debug', 'build/examples/tutorial/ns3.28-fifth-debug', 'build/examples/tutorial/ns3.28-sixth-debug', 'build/examples/tutorial/ns3.28-seventh-debug', 'build/examples/stats/ns3.28-wifi-example-sim-debug', 'build/examples/traffic-control/ns3.28-traffic-control-debug', 'build/examples/traffic-control/ns3.28-queue-discs-benchmark-debug', 'build/examples/traffic-control/ns3.28-red-vs-fengadaptive-debug', 'build/examples/traffic-control/ns3.28-red-vs-nlred-debug', 'build/examples/traffic-control/ns3.28-tbf-example-debug', 'build/examples/socket/ns3.28-socket-bound-static-routing-debug', 'build/examples/socket/ns3.28-socket-bound-tcp-static-routing-debug', 'build/examples/socket/ns3.28-socket-options-ipv4-debug', 'build/examples/socket/ns3.28-socket-options-ipv6-debug', 'build/examples/wireless/ns3.28-mixed-wired-wireless-debug', 'build/examples/wireless/ns3.28-wifi-adhoc-debug', 'build/examples/wireless/ns3.28-wifi-clear-channel-cmu-debug', 'build/examples/wireless/ns3.28-wifi-ap-debug', 'build/examples/wireless/ns3.28-wifi-wired-bridging-debug', 'build/examples/wireless/ns3.28-multirate-debug', 'build/examples/wireless/ns3.28-wifi-simple-adhoc-debug', 'build/examples/wireless/ns3.28-wifi-simple-adhoc-grid-debug', 'build/examples/wireless/ns3.28-wifi-simple-infra-debug', 'build/examples/wireless/ns3.28-wifi-simple-interference-debug', 'build/examples/wireless/ns3.28-wifi-blockack-debug', 'build/examples/wireless/ns3.28-ofdm-validation-debug', 'build/examples/wireless/ns3.28-ofdm-ht-validation-debug', 'build/examples/wireless/ns3.28-ofdm-vht-validation-debug', 'build/examples/wireless/ns3.28-wifi-hidden-terminal-debug', 'build/examples/wireless/ns3.28-ht-wifi-network-debug', 'build/examples/wireless/ns3.28-vht-wifi-network-debug', 'build/examples/wireless/ns3.28-wifi-timing-attributes-debug', 'build/examples/wireless/ns3.28-wifi-sleep-debug', 'build/examples/wireless/ns3.28-power-adaptation-distance-debug', 'build/examples/wireless/ns3.28-power-adaptation-interference-debug', 'build/examples/wireless/ns3.28-rate-adaptation-distance-debug', 'build/examples/wireless/ns3.28-wifi-aggregation-debug', 'build/examples/wireless/ns3.28-simple-ht-hidden-stations-debug', 'build/examples/wireless/ns3.28-80211n-mimo-debug', 'build/examples/wireless/ns3.28-mixed-network-debug', 'build/examples/wireless/ns3.28-wifi-tcp-debug', 'build/examples/wireless/ns3.28-80211e-txop-debug', 'build/examples/wireless/ns3.28-wifi-spectrum-per-example-debug', 'build/examples/wireless/ns3.28-wifi-spectrum-per-interference-debug', 'build/examples/wireless/ns3.28-wifi-spectrum-saturation-example-debug', 'build/examples/wireless/ns3.28-ofdm-he-validation-debug', 'build/examples/wireless/ns3.28-he-wifi-network-debug', 'build/examples/wireless/ns3.28-wifi-multi-tos-debug', 'build/examples/wireless/ns3.28-wifi-backward-compatibility-debug', 'build/examples/udp-client-server/ns3.28-udp-client-server-debug', 'build/examples/udp-client-server/ns3.28-udp-trace-client-server-debug', 'build/examples/ipv6/ns3.28-icmpv6-redirect-debug', 'build/examples/ipv6/ns3.28-ping6-debug', 'build/examples/ipv6/ns3.28-radvd-debug', 'build/examples/ipv6/ns3.28-radvd-two-prefix-debug', 'build/examples/ipv6/ns3.28-test-ipv6-debug', 'build/examples/ipv6/ns3.28-fragmentation-ipv6-debug', 'build/examples/ipv6/ns3.28-fragmentation-ipv6-two-MTU-debug', 'build/examples/ipv6/ns3.28-loose-routing-ipv6-debug', 'build/examples/ipv6/ns3.28-wsn-ping6-debug', 'build/examples/routing/ns3.28-dynamic-global-routing-debug', 'build/examples/routing/ns3.28-static-routing-slash32-debug', 'build/examples/routing/ns3.28-global-routing-slash32-debug', 'build/examples/routing/ns3.28-global-injection-slash32-debug', 'build/examples/routing/ns3.28-simple-global-routing-debug', 'build/examples/routing/ns3.28-simple-alternate-routing-debug', 'build/examples/routing/ns3.28-mixed-global-routing-debug', 'build/examples/routing/ns3.28-simple-routing-ping6-debug', 'build/examples/routing/ns3.28-manet-routing-compare-debug', 'build/examples/routing/ns3.28-ripng-simple-network-debug', 'build/examples/routing/ns3.28-rip-simple-network-debug', 'build/examples/routing/ns3.28-global-routing-multi-switch-plus-router-debug', 'build/examples/matrix-topology/ns3.28-matrix-topology-debug', 'build/examples/energy/ns3.28-energy-model-example-debug', 'build/examples/energy/ns3.28-energy-model-with-harvesting-example-debug', 'build/examples/error-model/ns3.28-simple-error-model-debug', 'build/scratch/subdir/ns3.28-subdir-debug', 'build/scratch/ns3.28-second-debug', 'build/scratch/ns3.28-scratch-simulator-debug', 'build/scratch/ns3.28-first-debug']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'realtime-udp-echo.py', 'first.py', 'second.py', 'third.py', 'mixed-wired-wireless.py', 'wifi-ap.py', 'simple-routing-ping6.py']

