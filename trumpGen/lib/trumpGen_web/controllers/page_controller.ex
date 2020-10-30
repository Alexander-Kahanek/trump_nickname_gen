defmodule TrumpGenWeb.PageController do
  use TrumpGenWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end
end
