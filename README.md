## python-logger

Two kinds of logger:
    - Default logger configured in file logging.yml
    - Wrapped logger uses a context filter to append additional information

How to use this API

```python
from logger import LoggerFactory

log = LoggerFactory.getDefaultLogger()
log.debug('DEBUG_LOG')
log.warning('HAHA_LOG')

log = LoggerFactory.getWrappedLogger(1, 2, 3)
log.warning('INFO_LOG')
log.info('INFO_LOG')
```