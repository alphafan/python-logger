import os
import yaml
import logging
import logging.config


class LoggerFactory(object):

    @staticmethod
    def getDefaultLogger():
        return LoggerFactory._getLogger('default')

    @staticmethod
    def getWrappedLogger(doc_id, task_id, industry):
        logger = LoggerFactory._getLogger('wrapped')
        filter = _ContextFilter(doc_id, task_id, industry)
        logger.addFilter(filter)
        return logger

    @staticmethod
    def _fileLogMaker():
        path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(path, 'bot.log')
        return logging.FileHandler(path)

    @staticmethod
    def _getLogger(name):
        # The file's path
        path = os.path.dirname(os.path.realpath(__file__))

        # Config file relative to this file
        loggingConf = open('{0}/logging.yml'.format(path), 'r')
        logging.config.dictConfig(yaml.load(loggingConf))
        loggingConf.close()
        logger = logging.getLogger(name)

        return logger


class _ContextFilter(logging.Filter):

    def __init__(self, doc_id, task_id, industry):
        self.doc_id = doc_id
        self.task_id = task_id
        self.industry = industry

    def filter(self, record):
        record.doc_id = self.doc_id
        record.task_id = self.task_id
        record.industry = self.industry
        return True

if __name__ == '__main__':
    log = LoggerFactory.getDefaultLogger()
    log.debug('DEBUG_LOG')
    log.warning('HAHA_LOG')

    log = LoggerFactory.getWrappedLogger(1, 2, 3)
    log.warning('INFO_LOG')
    log.info('INFO_LOG')
