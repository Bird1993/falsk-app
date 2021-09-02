package _Self.buildTypes

import jetbrains.buildServer.configs.kotlin.v2019_2.*

object BuildImage : BuildType({
    name = "build_image"

    artifactRules = """
        Dockerfile => /opt/teamcity-agent/artifacts/app
        requirements.txt => /opt/teamcity-agent/artifacts/app
    """.trimIndent()
    publishArtifacts = PublishMode.SUCCESSFUL

    vcs {
        root(AbsoluteId("Webapp_Git"))
    }

    steps {
        dockerCommand {
            name = "build_image"
            commandType = build {
                source = file {
                    path = "Dockerfile"
                }
                namesAndTags = "webapp:%build.number%"
            }
        }
    }
})
