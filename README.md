# Python RTI Example

[![codecov](https://codecov.io/gh/codecov/python-rti-example/branch/main/graph/badge.svg?token=pjzL5RLQL1)](https://codecov.io/gh/codecov/python-rti-example)

A repository demonstrating how to use Codecov's [Runtime Insights](https://about.codecov.io/product/feature/runtime-insights/) feature with the Flask framework. This example repository leverages the [codecov/python-codecov-opentelemetry](https://github.com/codecov/python-codecov-opentelemetry) package to send information to Codecov's Runtime Insights API. It is recommended to view the README for that package to learn more about Runtime Insights.

This repository is not intended to be used directly, but rather referred to as a reference for how to integrate Runtime Insights into your own python projects.

## Requirements and Pre-requisites

1. A repository that is active on [Codecov](https://codecov.io)
2. A profiling token obtainable from Codecov.
3. python version >=3

A profiling token can be obtained by applying to and being selected for our [Runtime Insights Early Access Program](https://about.codecov.io/product/feature/runtime-insights/).

### Codecov.yml Configuration

Some configuration is required in the `codecov.yml` to see Runtime Insights results in Pull Request comments. The full specification can be [found in our public documentation](https://docs.codecov.com/docs/runtime-insights#codecovyml-configuration), but the minimum is as follows:

```
comment:
  layout: "reach,diff,flags,tree,betaprofiling"
    show_critical_paths: true
```

Providing these settings in the `codecov.yml` will ensure that impacted files are marked as critical and impacted entrypoints are also shown in the Pull Request comment.
