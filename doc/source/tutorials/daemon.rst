Shaman's CLI
=========

Module bin/daemon.py is used to run workers. Options::

    usage: daemon.py [-h] [-i | -d] -c CONFIGURATION [--drop_first DROP_FIRST]
                     [-p PRINT_FIELDS [PRINT_FIELDS ...]]
                     [-r REMOVE_FIELDS [REMOVE_FIELDS ...]]
                     [--ignore_after IGNORE_AFTER]
                     [{stop,start,restart,} [{stop,start,restart,} ...]]

    Main shaman module. Use it to start|stop|restart daemon or start non-daemon
    modes of shaman

    positional arguments:
    {stop,start,restart,}
                            Command to daemon (default: )

    optional arguments:
    -h, --help            show this help message and exit
    -i                    Use stdin input as main input (default: False)
    -d                    Daemonize main process (default: False)
    -c CONFIGURATION      Path to configuration file (default: None)
    --drop_first DROP_FIRST  drop first lines (default: 0)
    -p PRINT_FIELDS [PRINT_FIELDS ...], --print_fields PRINT_FIELDS [PRINT_FIELDS ...]
    -r REMOVE_FIELDS [REMOVE_FIELDS ...], --remove_fields REMOVE_FIELDS [REMOVE_FIELDS ...]
    --ignore_after IGNORE_AFTER

Examples:
    1. Run shaman, reading from an stdin::

    cat urls.txt | python bin/daemon.py -c etc/crawler.config -i

Options here: -c <configuration_file>, -i (reading from stdin - True. Default is False)

    2. Run shaman, reading from kafka topic in a daemon mode::

    python bin/daemon.py -c etc/crawler_kafka.config start -d