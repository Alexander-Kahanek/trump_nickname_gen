defmodule Siample.NicknameChannel do
  require Logger

  use Phoenix.Channel

    def join("nickname", payload, socket) do
      {:ok, socket}
    end

    # def handle_in("nickname:broadcast", payload, socket) do
    #   Logger.info(":: Nickname:Broadcast recieve a message!::")
    #   broadcast! socket, "nickname:alert", payload
    #   {:noreply, socket}
    # end

end
