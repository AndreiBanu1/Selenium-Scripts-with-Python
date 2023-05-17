import pytest


class TestNGListenerExample:
    @pytest.hookimpl(tryfirst=True)
    def pytest_runtest_protocol(self, item, nextitem):
        print(f"Test Started: {item.nodeid}")
        nextitem()
        print(f"Test Finished: {item.nodeid}")

    def pytest_runtest_logreport(self, report):
        if report.when == "call" and report.passed:
            print(f"Test Passed: {report.nodeid}")
        elif report.when == "call" and report.failed:
            print(f"Test Failed: {report.nodeid}")
        elif report.when == "call" and report.skipped:
            print(f"Test Skipped: {report.nodeid}")

    def pytest_sessionstart(self, session):
        print(f"Test Suite Started: {session.name}")

    def pytest_sessionfinish(self, session, exitstatus):
        print(f"Test Suite Finished: {session.name}")


class TestNGListenerTestCase:
    def test_method1(self):
        print("Executing Test Method 1")
        assert 2 + 2 == 4

    def test_method2(self):
        print("Executing Test Method 2")
        assert True

    def test_method3(self):
        print("Executing Test Method 3")
        pytest.fail("Test Failed")


if __name__ == '__main__':
    pytest.main(args=[__file__, '-s'], plugins=[TestNGListenerExample()])
