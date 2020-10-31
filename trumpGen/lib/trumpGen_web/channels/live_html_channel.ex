defmodule TrumpGen.LiveHTMLChannel do
  use Phoenix.Channel

  require Logger

  def join("live-html", _message, socket) do
    {:ok, socket}
  end

  @spec handle_in(<<_::104>>, map, Phoenix.Socket.t()) :: {:noreply, Phoenix.Socket.t()}
  def handle_in("generate_name", %{"gen" => "gen", "text" => text}, socket) do

    name = TrumpGen.ModelPredictor.predict(text) |> to_string()

    html = Phoenix.View.render_to_string(TrumpGenWeb.PageView, "generate.html", text: name)

    broadcast!(socket, "live_response", %{html: html})
    {:noreply, socket}
  end
end
