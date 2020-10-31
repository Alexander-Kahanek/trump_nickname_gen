defmodule TrumpGen.PythonHelper do
  require Logger


  def py_instance(path) when is_binary(path) do
    {:ok, pid} = :python.start([{:python_path, to_charlist(path)}])
    pid
  end

  @spec py_call(atom | pid | {atom, any} | {:via, atom, any}, atom, atom, [any]) :: :ok
  def py_call(pid, module, func, args \\ []) do
    name = pid |> :python.call(module, func, [args])
    name
  end

  def py_stop(pid) do
    :python.stop(pid)
  end
end
