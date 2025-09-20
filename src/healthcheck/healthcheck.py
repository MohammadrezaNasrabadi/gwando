class HealthCheck:
    status = True

    @staticmethod
    def get_status() -> bool:
        return HealthCheck.status

    @staticmethod
    def set_status(status: bool):
        HealthCheck.status = status
