defmodule PhoenixLiveHtml.LiveHTMLChannel do
  use Phoenix.Channel

  def join("live-html", _message, socket) do
    {:ok, socket}
  end

  def handle_in("generate_name", %{"gen" => gen, "text" => text},
    socket) do
      html = Phoenix.View.render_to_string(PhoenixLiveHtml.PageView, "generate.html", text: text)

      broadcast!(socket, "live_response", %{html: html})
      {:noreply, socket}
    end
end
