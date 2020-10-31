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
  secret_key_base: "FY4AvBqGt82I+4iCJag8GvbME7//ALN0oVsu6CKNGg1DLWFd3V9DvVSbxQUJiq3L",
  render_errors: [view: TrumpGenWeb.ErrorView, accepts: ~w(html json), layout: false],
  pubsub_server: TrumpGen.PubSub,
  live_view: [signing_salt: "hryF6qwX"]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"
