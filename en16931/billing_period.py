"""
Class for representing a billing period.
"""
import datetime

class BillingPeriod:
    def __init__(self, start=None, end=None):
        if start > end:
            raise ValueError('Billing period start date must not be later than billing period end date')
        self._start = self._foo(start)
        self._end = self._foo(end)

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, start):
        if start > self._end:
            raise ValueError('Billing period start date must not be later than billing period end date')
        self._start = self._foo(start)

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        if end < self._start:
            raise ValueError('Billing period end date must not be earlier than billing period start date')
        self._end = self._foo(end)

    def _foo(self, date):
        if isinstance(date, datetime.datetime) or isinstance(date, datetime.date):
            return date
        if isinstance(date, str):
            return parse_date(date)
        raise ValueError("Unrecognized date")
