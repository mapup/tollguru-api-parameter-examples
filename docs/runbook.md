# Runbook

## How to Recover from Common Failures

### API Authentication Failures
- **Issue**: Invalid API key or expired credentials
- **Recovery**: Replace placeholder API keys with valid keys from TollGuru dashboard
- **Verification**: Test with a simple API call using provided examples

### Invalid Request Parameters
- **Issue**: Malformed JSON or invalid parameter combinations
- **Recovery**: Reference the provided examples and compare with API documentation
- **Verification**: Use JSON validators to check request syntax

### Rate Limiting
- **Issue**: Too many API requests in short time period
- **Recovery**: Implement exponential backoff and respect rate limits
- **Monitoring**: Check HTTP 429 responses

## Rollback Basics

Since this is a static repository of examples, rollback involves:
- Reverting changes via git: `git reset --hard HEAD~1`
- Restoring from backup if JSON examples become corrupted
- No database or service rollbacks required

## On-Call / Logs / Monitoring Entry Points

### Monitoring
- GitHub repository activity (issues, PRs, commits)
- Example file integrity checks
- Link validation to external API documentation

### Logs
- GitHub Actions workflow logs for any automated checks
- No application logs as this is a static repository

### On-Call Procedures
- Monitor GitHub issues for user-reported problems with examples
- Validate examples against API changes
- Update examples when API endpoints are modified

## Cron Jobs / Scheduled Jobs

No scheduled jobs are currently implemented. Potential future automation:
- Weekly validation of examples against TollGuru API
- Automated link checking for external documentation
- Example freshness checks

## Data Backfill Scripts

Not applicable - this repository contains static examples only. No data backfilling is required.

## Emergency Procedures

### Example Corruption
- If JSON examples become corrupted, restore from git history
- Validate all examples using JSON schema validators
- Test restored examples against live API

### Documentation Updates
- When TollGuru API changes, update examples accordingly
- Coordinate with API team for breaking changes
- Version examples if multiple API versions are supported
