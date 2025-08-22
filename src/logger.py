"""Centralized logging component for TOBE MCP Server."""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


class TOBELogger:
    """Centralized logger for TOBE MCP Server."""
    
    def __init__(self, name: str = "tobe-mcp", level: int = logging.INFO, log_file: Optional[str] = None):
        self.name = name
        self.level = level
        self.log_file = log_file
        
        # Create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.handlers.clear()
        
        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(filename)s:%(lineno)d | %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler
        if log_file:
            self._setup_file_handler(log_file, formatter)
        
        self.logger.propagate = False
    
    def _setup_file_handler(self, log_file: str, formatter: logging.Formatter):
        try:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)
            
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(self.level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except Exception as e:
            self.logger.error(f"Failed to setup file logging: {e}")
    
    def debug(self, message: str, *args, **kwargs):
        self.logger.debug(message, *args, **kwargs)
    
    def info(self, message: str, *args, **kwargs):
        self.logger.info(message, *args, **kwargs)
    
    def warning(self, message: str, *args, **kwargs):
        self.logger.warning(message, *args, **kwargs)
    
    def error(self, message: str, *args, **kwargs):
        self.logger.error(message, *args, **kwargs)
    
    def critical(self, message: str, *args, **kwargs):
        self.logger.critical(message, *args, **kwargs)
    
    def exception(self, message: str, *args, **kwargs):
        self.logger.exception(message, *args, **kwargs)
    
    def log_tool_call(self, tool_name: str, arguments: dict, success: bool, duration: float = None):
        status = "SUCCESS" if success else "FAILED"
        duration_str = f" ({duration:.3f}s)" if duration is not None else ""
        self.info(f"Tool call: {tool_name} | Status: {status} | Args: {arguments}{duration_str}")
    
    def log_server_event(self, event: str, details: dict = None):
        details_str = f" | Details: {details}" if details else ""
        self.info(f"Server event: {event}{details_str}")
    
    def log_performance(self, operation: str, duration: float, additional_info: dict = None):
        """Log performance metrics."""
        info_str = f" | Info: {additional_info}" if additional_info else ""
        self.info(f"Performance: {operation} | Duration: {duration:.3f}s{info_str}")


# Global logger instance
_logger_instance: Optional[TOBELogger] = None


def get_logger(name: str = "tobe-mcp", level: int = logging.INFO, log_file: Optional[str] = None) -> TOBELogger:
    if log_file is None:
        log_file = Path(__file__).parent.parent / "logs" / "tobe-mcp.log"
    
    return TOBELogger(name=name, level=level, log_file=str(log_file))


def setup_logging(level: str = "INFO", log_file: Optional[str] = None) -> TOBELogger:
    level_map = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }
    
    log_level = level_map.get(level.upper(), logging.INFO)
    return get_logger("tobe-mcp", log_level, log_file)


# Global default logger for convenience functions
_default_logger = None

def _get_default_logger():
    global _default_logger
    if _default_logger is None:
        _default_logger = get_logger()
    return _default_logger

# Convenience functions
def debug(message: str, *args, **kwargs):
    _get_default_logger().debug(message, *args, **kwargs)


def info(message: str, *args, **kwargs):
    _get_default_logger().info(message, *args, **kwargs)


def warning(message: str, *args, **kwargs):
    _get_default_logger().warning(message, *args, **kwargs)


def error(message: str, *args, **kwargs):
    _get_default_logger().error(message, *args, **kwargs)


def critical(message: str, *args, **kwargs):
    _get_default_logger().critical(message, *args, **kwargs)


def exception(message: str, *args, **kwargs):
    _get_default_logger().exception(message, *args, **kwargs) 