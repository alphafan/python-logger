## python-logger

Two kinds of logger:
   - Default logger configured in file logging.yml
   - Wrapped logger uses a context filter to append additional information

How to use this API ?

```python
from logger import LoggerFactory

log = LoggerFactory.getDefaultLogger()
log.debug('Default log debug')
log.warning('Default log warning')

log = LoggerFactory.getWrappedLogger(1, 2, 3)
log.warning('Wrapped warning')
log.info('Wrapped info')
```

Example output:

"""
2018-01-13 20:54:13 DEBUG    [logger.py:59] Default log debug
2018-01-13 20:54:13 WARNING  [logger.py:60] Default log warning
2018-01-13 20:54:13 WARNING  [logger.py:63] [doc_id:1|task_id:2|industry:3] Wrapped warning
2018-01-13 20:54:13 INFO     [logger.py:64] [doc_id:1|task_id:2|industry:3] Wrapped info
"""