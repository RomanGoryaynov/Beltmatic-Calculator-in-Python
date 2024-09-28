def generate_expressions(target_number, max_size, operations, max_number, exclude_numbers=None):
  """
  Генерирует список выражений для заданного целевого числа.

  Args:
    target_number: Целевое число для которого нужно сгенерировать выражения.
    max_size: Максимальное количество операций в выражении.
    operations: Список допустимых операций (например, ["+", "-", "*", "/"]).
    max_number: Максимальное число, которое можно использовать в выражении.
    exclude_numbers: Список чисел, которые нужно исключить из выражений.

  Returns:
    Список выражений, которые могут быть вычислены до целевого числа.
  """

  expressions = []

  def generate_expression(current_number, size, expression):
    """
    Рекурсивная функция для генерации выражений.

    Args:
      current_number: Текущее значение, вычисляемое в выражении.
      size: Текущий размер выражения (количество операций).
      expression: Строка, представляющая текущее выражение.

    Returns:
      None.
    """
    if size == max_size:
      if current_number == target_number:
        # Проверяем, не исключено ли текущее число:
        expressions.append(expression)
      return

    

    for op in operations:
      for num in range(min_number, max_number + 1):
        new_expression = f"{expression}{op}{num}"
        new_current_number = eval(new_expression)
        if new_current_number <= target_number:
          generate_expression(new_current_number, size + 1, new_expression)



  # Изменяем начальный размер выражения:
  for start_number in range(min_number, max_number + 1):  # Проходим по всем числам от 1 до max_number
    for size in range(max_size + 1):
      generate_expression(start_number, size, str(start_number))

  return expressions

# Пример использования:
target_number = 12
max_size = 2
operations = ["+", "*"]
max_number = 4
min_number = 1

expressions = generate_expressions(target_number, max_size, operations, max_number, min_number)

print(f"{target_number} -> ({len(expressions)}) {expressions}")
