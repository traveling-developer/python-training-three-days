class InsurancePolicy:
    def __init__(self, age, is_smoker, base_premium=500):
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")
        self.base_premium = base_premium
        self.age = age
        self.is_smoker = is_smoker

    def get_age_adjustment(self):
        return self.base_premium * 0.2 if self.age > 50 else 0

    def get_smoker_adjustment(self):
        return self.base_premium * 0.3 if self.is_smoker else 0

    def calculate_premium(self):
        return (
            self.base_premium
            + self.get_age_adjustment()
            + self.get_smoker_adjustment()
        )
