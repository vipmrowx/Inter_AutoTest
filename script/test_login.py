import pytest
import allure


class TestLogin:
    @allure.severity("normal")
    def test_login1(self):
        assert 1

    @allure.severity("critical")
    def test_login2(self):
        assert 0

    @allure.severity("blocker")
    def test_login3(self):
        assert 0

