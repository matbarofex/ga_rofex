# coding: utf-8


class PMYAPIException(Exception):

    def __init__(self, msg, e=None):
        self.msg = msg
        self.exception = e

    def __str__(self):
        return "message: " + self.msg + "; exception: " + self.exception

