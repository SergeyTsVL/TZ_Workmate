import sys

import pytest
import tempfile
from main import Analiz_logs




# class TestAnaliz_logs:
# def test_print_table_tabulate():
#     with tempfile.NamedTemporaryFile(mode='w') as tmp_file:
#         data = [['/admin/dashboard/', '1', '0', '0', '0', '0']]
#         f = Analiz_logs()
#         f.print_table_tabulate(data)
#         a = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL')
#         i = str(a)
#         d = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format('/admin/dashboard/', '1', '0', '0', '0', '0')
#         with open(tmp_file.name, 'r') as f:
#             assert f.read() == f'Total requests:{0}\n{i}\n{d}'

# from io import StringIO
# import sys
#
#
# def test_print_table_tabulate():
#     # Set up StringIO buffer
#     output_buffer = StringIO()
#
#     # Save original stdout
#     original_stdout = sys.stdout
#
#     try:
#         # Redirect stdout to buffer
#         sys.stdout = output_buffer
#
#         # Test setup
#         data = [['/admin/dashboard/', '1', '0', '0', '0', '0']]
#         f = Analiz_logs()
#
#         # Call the method being tested
#         f.print_table_tabulate(data)
#
#         # Get captured output
#         captured_output = output_buffer.getvalue()
#
#         # Expected output strings
#         header = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(
#             'HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'
#         )
#         data_row = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(
#             '/admin/dashboard/', '1', '0', '0', '0', '0'
#         )
#
#         # Verify contents
#         assert captured_output == f'Total requests:{0}\n{header}\n{data_row}'
#
#     finally:
#         # Restore stdout regardless of test outcome
#         sys.stdout = original_stdout

# def test_print_table_tabulate(capsys):
#     data = [['/admin/dashboard/', '1', '0', '0', '0', '0']]
#     f = Analiz_logs()
#
#     # Call the method being tested
#     f.print_table_tabulate(data)
#
#     # Get captured output
#     captured = capsys.readouterr()
#
#     # Expected output strings
#     header = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(
#         'HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'
#     )
#     data_row = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(
#         '/admin/dashboard/', '1', '0', '0', '0', '0'
#     )
#
#     assert captured.out == f'Total requests:{0}\n{header}\n{data_row}'


def test_print_table_tabulate(capsys):
    data = [['/admin/dashboard/', '1', '0', '0', '0', '0']]
    f = Analiz_logs()

    # Call the method being tested
    f.print_table_tabulate(data)

    # Get captured output
    captured = capsys.readouterr()

    print("=== Captured Output ===")
    print(captured.out)
    print("\n=== Expected Output ===")
    header = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(
        'HANDLER', 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'
    )
    data_row = '{:<30}{:<15}{:<15}{:<15}{:<15}{:<15}'.format(
        '/admin/dashboard/', '1', '0', '0', '0', '0'
    )
    expected = f'Total requests:{0}\n{header}\n{data_row}'
    print(expected)

    assert captured.out == expected



# pytest test_main.py::test_data_saved
# pytest test_main.py
# pytest -v

