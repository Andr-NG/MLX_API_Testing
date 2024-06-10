from services.PAM.endpoints.PAM import PAM


class BaseTest:

    def setup_method(self):
        self.PAM = PAM()
