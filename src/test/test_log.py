import logging
from unittest.mock import Mock, patch

import pytest

from activitypub_event_server import log


@pytest.mark.parametrize(
    ["m_file_path", "expected_class"],
    [[None, logging.StreamHandler], ["test.log", logging.FileHandler]],
)
def test_setup_func_exception_log_handler_file_handler(m_file_path, expected_class):
    """Test that the setup_func_exception_log_handler function returns the correct handler."""
    m_log_level = logging.INFO
    m_func_name = "test_func"
    m_format_str = "%(asctime)s - %(name)s: %(funcName)s - %(levelname)s - %(message)s"

    with patch(
        "activitypub_event_server.log.FuncNameExceptionFilter", autospec=True
    ) as m_func_name_filter:
        # Setup handler and check that it is the correct class
        handler = log.setup_func_exception_log_handler(
            m_func_name, m_file_path, m_log_level, m_format_str
        )
        assert isinstance(handler, expected_class)

        # Check that handler has correct level and format
        assert handler.level == m_log_level
        assert handler.formatter._fmt == m_format_str

        # Make sure the filter was added to the handler
        m_func_name_filter.assert_called_once_with(m_func_name, m_log_level)


def test_func_name_exception_filter():
    """Test that the FuncNameExceptionFilter filter works as expected."""
    m_func_name = "test_func"
    m_log_level = logging.INFO
    m_record = Mock(funcName=m_func_name, levelno=m_log_level)

    # Test that the filter returns True when the record has the correct funcName and level
    filter = log.FuncNameExceptionFilter(m_func_name, m_log_level)
    assert filter.filter(m_record)

    # Test that the filter returns False when the record has the correct funcName but the wrong level
    m_record.levelno = logging.DEBUG
    assert not filter.filter(m_record)

    # Test that the filter returns False when the record has the wrong funcName but the correct level
    m_record.funcName = "wrong_func"
    m_record.levelno = m_log_level
    assert not filter.filter(m_record)

    # Test that the filter returns False when the record has the wrong funcName and the wrong level
    m_record.funcName = "wrong_func"
    m_record.levelno = logging.DEBUG
    assert not filter.filter(m_record)
