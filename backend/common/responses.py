from rest_framework.response import Response


def response_success(message, results, status=200):
    return Response({"message": message, "results": results}, status=status)


def response_error(message, error, status=500):
    return Response({"message": message, "error": error}, status=status)
