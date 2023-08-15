import string
import numpy as np


class Calculator:
    def get_fractions(self, frac_str: (int or float or string)) -> (int or float):
        """Checks a number and returns to float type.

        Parameters
        ----------
        frac_str : int or float or string
            Number in int, float or string type.

        Returns
        -------
        float
            Fixed float type number.
        """

        if isinstance(frac_str, (int, float)):
            return frac_str

        if "/" not in frac_str:
            return float(frac_str)
        try:
            return float(frac_str)
        except ValueError:
            num, denom = frac_str.split("/")
            try:
                leading, num = num.split(" ")
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac


    def sum(self, a: any, b: any) -> (int or float):
        """Gets two numbers, adds them, and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the sum.
        """

        sum_a = self.get_fractions(a)
        sum_b = self.get_fractions(b)
        return np.sum([sum_a, sum_b])


    def subtract(self, a: any, b: any) -> (int or float):
        """Gets two numbers, subtracts the second from the first,
        and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the substraction.
        """

        minuend = self.get_fractions(a)
        subtrahend = self.get_fractions(b)
        return minuend - subtrahend


    def multiply(self, a: any, b: any) -> (int or float):
        """Gets two numbers, multiplies them, and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the multiplication.
        """

        multiplicand = self.get_fractions(a)
        multiplier = self.get_fractions(b)
        return multiplicand * multiplier


    def divide(self, a: any, b: any) -> (int or float):
        """Gets two numbers, divide the first by the second,
        and returns the result.

        Parameters
        ----------
        a : any
            Number in int or float type.
        b : any
            Number in int or float type.

        Returns
        -------
        any
            Result of the division.
        """

        dividend = self.get_fractions(a)
        divider = self.get_fractions(b)
        
        try:
            return np.divide(dividend, divider)
        except ZeroDivisionError:
            return "Division by zero is not allowed!"