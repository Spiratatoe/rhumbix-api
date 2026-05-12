# Endpoint sample payloads (anonymized)

One JSON file per Rhumbix endpoint, each containing the **response shape**
captured from a live `GET` against the tenant's API. Values have been
replaced — see "What was changed" below.

These exist so a reader can see the exact field set, nesting, and types
each endpoint returns without making a live call.

## What was changed

Every file went through `anonymize_samples.py`. Replacements:

| Field family | Real | Fake (deterministic) |
|---|---|---|
| `email`, `*_email` | `m.bachmann@tcco.com` | `riley.vance@example.com` |
| `first_name`, `last_name` | `Adan`, `Morales` | `Sawyer`, `Vance` |
| `phone`, `*_phone`, `phone_number` | `+12107129150` | `+17357026010` |
| `address`, `*_address` | `700 Aquarena Springs Dr, San Marcos, TX` | `4487 Aspen Ln, Riverton, TX 78700, USA` |
| `client_name`, `client_contact_*` | real client / contact | fake company name / contact |
| `employee`, `foreman`, `creator`, `worker`, `company_supplied_id`, etc. | `703828` | `630009` (digit count preserved) |
| `employees[]`, `employee_permissions[]`, etc. | `[703828, ...]` | each ID mapped to its fake equivalent |
| `job_number` / `job_numbers[]` / `project_id` | `240676` | `339823` (6 digits) |
| `cost_code` | `240676.01.01.65.657940L` | `962391.10.11.15.471836L` (dot structure + alpha suffix preserved) |
| `work_shift_key` | `5xD2A8L5` | `7VADPKRQ` (length preserved) |
| Any key containing `uuid` / value that looks like a UUID | `2a8ef4ae-...` | a deterministic fake UUID |
| `cico_pin` / `cico_qr_code` | `12345` / `abc...` | fake 4-digit / 8-char codes |
| Any URL with `AWSAccessKeyId=`, `X-Amz-*`, `Signature=` | real signed S3 URL | `https://example.com/files/<hash>.jpg` |
| URL-shaped keys (`fullsize`, `thumbnail`, `photo`, `*_url`) | real URL | `https://example.com/files/<hash>.jpg` |
| `name` on `projects` / `cohorts` / `companies` / `company_groups` | real label | fake label of the right kind |
| `description` on `projects` | real | `"Sample project description"` |

What was **not** changed (these aren't PII and matter for shape/realism):

- `created_on`, `last_updated`, `start_time`, `end_time`, `shift_date`, and other ISO datetime strings
- `status`, `user_role`, `timezone`, `signature_period`, etc.
- All booleans, all numbers (durations, prices, integer IDs like row `id`)
- Empty strings (`""`), `null`, and empty lists/objects — preserved exactly
- Resource enums and trade names

### Mapping is deterministic and cross-file consistent

The anonymizer seeds every fake from the real value via SHA-1, so:

- Re-running the script reproduces the same fake values.
- The same real ID becomes the same fake ID in every file. For example, foreman `709215` in `timekeeping_entries.json` maps to the same fake ID that appears in `cohorts.json#employees`, `employees.json#company_supplied_id`, etc.

If you change the salt in `SEED` and re-run, you get a new mapping but with the same property.

## Coverage

`_index.json` lists the row count per resource. A few resources came back
with `0 rows` because this tenant doesn't have records for them right now
(e.g., `equipment`, `notes`, `quantity_entries`, `companies`). A handful
returned `404` from the API and aren't represented at all
(`users`, `groups`, `field_folders`, `field_folder_notes`,
`timeoff_requests`, `company_classifications`, `company_trades`,
`cost_code_controls`) — those endpoints may not exist on this tenant or
need a tenant-specific path.

The first record from `employees` (and similar resources) was the Rhumbix
admin user; the anonymizer drops obvious admin/test rows when at least
three non-admin rows are available, so what you see is a regular-user
sample.

## Reproducing

```bash
.venv\Scripts\python.exe capture_samples.py    # writes output/samples/
.venv\Scripts\python.exe anonymize_samples.py  # writes this directory
```

The capture step requires a working `.env`; the anonymize step works
offline against `output/samples/`.
