# Jenkinsfile Variants for Website Deployment

This repository contains multiple `Jenkinsfile` variations for deploying a website. Each `Jenkinsfile` represents a different deployment strategy or configuration, allowing for flexibility and experimentation.

## Purpose

The purpose of this repository is to:

* Demonstrate different ways to deploy a website using Jenkins pipelines.
* Provide examples of common Jenkins pipeline patterns.
* Enable easy switching between deployment configurations.
* Facilitate experimentation and testing of deployment changes.

## Repository Structure

## Prerequisites

* Jenkis installed and configured in each agent/node 
* Each node has git installed and configured
* Each node has GITHUB_PAT configured as env variable
* Eacn node has docker installed 
* Each node has configured jenkins user as part of docker gruop to execute docker commands