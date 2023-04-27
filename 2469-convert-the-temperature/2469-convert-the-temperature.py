class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius+273.15,(1.80*celsius)+32.00]
        