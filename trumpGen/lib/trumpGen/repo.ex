defmodule TrumpGen.Repo do
  use Ecto.Repo,
    otp_app: :trumpGen,
    adapter: Ecto.Adapters.Postgres
end
