import sys
import time

def evaluate_condition(condition, variables):
    try:
        for var in variables:
            condition = condition.replace(var, str(variables[var]))
        return eval(condition)
    except:
        return False

def execute(code_lines, variables=None, functions=None):
    if variables is None:
        variables = {}
    if functions is None:
        functions = {}

    i = 0
    while i < len(code_lines):
        line = code_lines[i].strip()
        parts = line.split()

        if not parts:
            i += 1
            continue

        command = parts[0].upper()

        if command == "SET" and len(parts) >= 3:
            var = parts[1]
            value = ' '.join(parts[2:])
            for v in variables:
                value = value.replace(v, str(variables[v]))
            try:
                variables[var] = int(eval(value))
            except:
                variables[var] = value

        elif command == "PRINT" and len(parts) == 2:
            var = parts[1]
            print(variables.get(var, f"Unknown variable: {var}"))

        elif command == "ADD" and len(parts) == 3:
            a = variables.get(parts[1], 0)
            b = variables.get(parts[2], 0)
            print(a + b)

        elif command == "INPUT" and len(parts) == 2:
            var = parts[1]
            value = input(f"Enter value for {var}: ")
            try:
                variables[var] = int(value)
            except:
                variables[var] = value

        elif command == "DEF" and len(parts) == 2:
            func_name = parts[1]
            func_lines = []
            i += 1
            while i < len(code_lines):
                inner = code_lines[i].strip()
                if inner.upper() == "END":
                    break
                func_lines.append(inner)
                i += 1
            functions[func_name] = func_lines

        elif command == "CALL" and len(parts) == 2:
            func_name = parts[1]
            if func_name in functions:
                execute(functions[func_name], variables.copy(), functions)
            else:
                print(f"Function {func_name} does not exist")

        elif command == "IF":
            cond = ' '.join(parts[1:])
            true_block = []
            false_block = []
            elif_blocks = []
            i += 1
            current_block = true_block
            while i < len(code_lines):
                inner = code_lines[i].strip()
                if inner.upper().startswith("ELSEIF"):
                    current_block = []
                    elif_blocks.append((inner[7:].strip(), current_block))
                elif inner.upper() == "ELSE":
                    current_block = false_block
                elif inner.upper() == "END":
                    break
                else:
                    current_block.append(inner)
                i += 1
            if evaluate_condition(cond, variables):
                execute(true_block, variables, functions)
            else:
                executed = False
                for elif_cond, elif_block in elif_blocks:
                    if evaluate_condition(elif_cond, variables):
                        execute(elif_block, variables, functions)
                        executed = True
                        break
                if not executed and false_block:
                    execute(false_block, variables, functions)

        elif command == "WHILE":
            cond = ' '.join(parts[1:])
            loop_block = []
            i += 1
            while i < len(code_lines):
                inner = code_lines[i].strip()
                if inner.upper() == "END":
                    break
                loop_block.append(inner)
                i += 1
            while evaluate_condition(cond, variables):
                execute(loop_block, variables, functions)

        elif command == "ALERT" and len(parts) >= 2:
            msg = ' '.join(parts[1:])
            print(f"ALERT: {msg}")

        elif command == "SLEEP" and len(parts) == 2:
            try:
                delay = float(parts[1])
                time.sleep(delay)
            except:
                print("Invalid value for SLEEP")

        elif command == "READFILE" and len(parts) == 3:
            var = parts[1]
            filename = parts[2]
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                variables[var] = content
            except FileNotFoundError:
                print(f"File {filename} not found")

        else:
            print(f"Unknown command: {line}")

        i += 1

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        filename = input("Enter filename (e.g. program.dex): ")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            program_lines = f.readlines()
        execute(program_lines)
    except FileNotFoundError:
        print(f"File '{filename}' does not exist")
