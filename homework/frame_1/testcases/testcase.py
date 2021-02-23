from homework.frame_1.app import APP


class  TestCases:
    def setup(self):
        self.main = APP().start_app()

    def teardown(self):
        self.main.stop_app()

    def test_blacklist(self):
        self.main.goto_main().goto_market()