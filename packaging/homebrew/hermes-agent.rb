# typed: false
# frozen_string_literal: true

# Legacy Homebrew compatibility formula for Doppel Agent.
class HermesAgent < Formula
  include Language::Python::Virtualenv

  desc "Your Everyday Personal AI Assistant with tools, memory, and messaging"
  homepage "https://github.com/Jnot1/doppel-agent"
  # Until the fork has its own published Homebrew release pipeline, both the
  # preferred Doppel formula and this legacy compatibility formula track the
  # latest upstream semver-named sdist asset.
  url "https://github.com/NousResearch/hermes-agent/releases/download/v2026.5.29.2/hermes_agent-0.15.2.tar.gz"
  sha256 "3192f8d5d11b1d368b8a8090d68a7fb0a1e485d991f99ff7ed98b53d93e5ce78"
  license "MIT"

  depends_on "certifi" => :no_linkage
  depends_on "cryptography" => :no_linkage
  depends_on "libyaml"
  depends_on "python@3.14"
  conflicts_with "jnot1/doppel-agent/doppel-agent", because: "both formulas install the same Doppel Agent executables"

  pypi_packages exclude_packages: %w[certifi cryptography pydantic]

  # Refresh resource stanzas after bumping the source url/version:
  #   brew update-python-resources --print-only hermes-agent

  def install
    venv = virtualenv_create(libexec, "python3.14")
    venv.pip_install resources
    venv.pip_install buildpath

    pkgshare.install "skills", "optional-skills"

    %w[doppel doppel-agent doppel-acp hermes hermes-agent hermes-acp].each do |exe|
      next unless (libexec/"bin"/exe).exist?

      (bin/exe).write_env_script(
        libexec/"bin"/exe,
        HERMES_BUNDLED_SKILLS:  pkgshare/"skills",
        HERMES_OPTIONAL_SKILLS: pkgshare/"optional-skills",
        HERMES_MANAGED:         "homebrew:hermes-agent",
      )
    end
  end

  test do
    assert_match "Doppel Agent v#{version}", shell_output("#{bin}/doppel version")
    assert_match "Doppel Agent v#{version}", shell_output("#{bin}/hermes version")

    managed = shell_output("#{bin}/doppel update 2>&1")
    assert_match "managed by Homebrew", managed
    assert_match "brew upgrade hermes-agent", managed
  end
end
