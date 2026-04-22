# Architecture

## Major Services

This repository is a static collection of API examples and does not contain running services. The examples interact with TollGuru's external API services.

## Datastore Choices

No datastores are used in this repository. All data is stored as static JSON files for API request/response examples.

## Queues/Jobs

No queues or job processing systems are implemented in this repository.

## Third-Party Dependencies

Dependencies are minimal and primarily for utility scripts:
- Python standard library (json, sys, os, urllib.parse) for the cURL conversion script
- No package.json dependencies as this is not a Node.js application

## Auth Model

This repository uses API key authentication for TollGuru services:
- API keys are passed via the `x-api-key` header
- Keys are placeholder values in examples and must be replaced with actual keys

## Tenancy Model

Not applicable - this is a multi-tenant example repository that serves all TollGuru API users.
