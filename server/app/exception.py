from rest_framework.views import exception_handler as _handler

def exception_handler(exc, context):
    response = _handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code

    return response

class TimeSlotConflict(Exception):
    pass

class OrderStatusIncorrect(Exception):
    pass

class RefundError(Exception):
    pass

class KuailexueDataError(Exception):
    pass

class KuailexueServerError(Exception):
    pass
