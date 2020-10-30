# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
use Mix.Config

config :trumpGen,
  ecto_repos: [TrumpGen.Repo]

# Configures the endpoint
config :trumpGen, TrumpGenWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "5D0Ydi25c4cMXV4edPvZUtXHUTvPFF8zUo/2fy8oXtzmuOz1EepUw0fIDucrCO00",
  render_errors: [view: TrumpGenWeb.ErrorView, accepts: ~w(html json), layout: false],
  pubsub_server: TrumpGen.PubSub,
  live_view: [signing_salt: "o5FIO1Kf"]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"
