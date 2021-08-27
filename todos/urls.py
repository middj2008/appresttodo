from django.urls import path
from todos.views import TodosListCreateAPIView, TodoDetailAPIView


urlpatterns = [
    path("", TodosListCreateAPIView.as_view(), name="todos"),
    path("<int:id>", TodoDetailAPIView.as_view(), name="todo"),
    # path('create', CreateTodoAPIView.as_view(), name="create-todo"),
    # path('list', TodoListAPIView.as_view(), name="list-todos"),
]