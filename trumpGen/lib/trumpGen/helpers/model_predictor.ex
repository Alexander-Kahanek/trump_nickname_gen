defmodule TrumpGen.ModelPredictor do
  @moduledoc false

  alias TrumpGen.PythonHelper, as: Helper
  require Logger

  @path 'priv/py38/'

  def predict(args) do
    result = call_python(:generate, :generate_name, args)
    result
  end

  defp call_python(module, func, args) do
    pid = Helper.py_instance(Path.absname(@path))
    result = Helper.py_call(pid, module, func, args)

    pid
    |> Helper.py_stop()

    result
  end
end
