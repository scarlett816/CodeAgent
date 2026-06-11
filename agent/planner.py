class Planner:

    def is_final(self, action: dict):

        if not isinstance(action, dict):
            return False

        return action.get("action") == "final"