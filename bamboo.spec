version: 2
plan:
  project-key: UL
  key: PLAN
  name: My Plan

stages:
  - Stage 1:
      jobs:
        - Job 1

Job 1:
  tasks:
    - script:
        - echo 'Hello from YAML Specs'
