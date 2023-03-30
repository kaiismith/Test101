class Calculator:
    def calculate_BMI(self, weight, height):
        self.BMI = weight / (height ** 2)
        return self.BMI

    def calculate_body_fat(self, age, weight, height, gender):
        self.BMI = Calculator().calculate_BMI(weight, height)

        if age < 18:
            self.body_fat = ((1.51 * self.BMI) - (0.7 * age) - (3.6 * gender) + 1.4)

        else:
            self.body_fat = ((1.2 * self.BMI) - (0.23 * age) - (10.8 * gender) - 5.4)

        return self.body_fat

    def calculate_LBM(self, weight, height, gender):
        if gender == 1:
            self.LBM = 0.407 * weight + 0.267 * height - 19.2
        else:
            self.LBM = 0.252 * weight + 0.473 * height - 48.3

        return self.LBM

    def calculate_BMR(self, weight, age, height, gender):
        if gender == 1:
            self.BMR = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        else:
            self.BMR = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)

        return self.BMR


