defmodule PhoenixLiveHtml.LiveHTMLChannel do
  use Phoenix.Channel

  def join("live-html", _message, socket) do
    {:ok, socket}
  end

<<<<<<< HEAD
  @spec handle_in(<<_::104>>, map, Phoenix.Socket.t()) :: {:noreply, Phoenix.Socket.t()}
  def handle_in("generate_name", %{"gen" => "gen", "text" => text}, socket) do

    name = TrumpGen.ModelPredictor.predict(text) |> to_string()

    Logger.debug("name was created: " <> name)

    html = Phoenix.View.render_to_string(TrumpGenWeb.PageView, "generate.html", text: name)
=======
  def handle_in("generate_name", %{"gen" => gen, "text" => text},
    socket) do
      html = Phoenix.View.render_to_string(PhoenixLiveHtml.PageView, "generate.html", text: text)
>>>>>>> parent of 6cef961... update need python

      broadcast!(socket, "live_response", %{html: html})
      {:noreply, socket}
    end
end
