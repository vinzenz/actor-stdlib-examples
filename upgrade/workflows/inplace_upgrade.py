from leapp.workflows import Workflow, Phase, Flags, Filter, TagFilter, Policies
from leapp.tags import IPUTag, FactsTag, CommonFactsTag, ChecksTag, CommonChecksTag, ChecksTag, CommonChecksTag, \
    AttachPackageReposTag, CommonAttachPackageReposTag, PlanningTag, CommonPlanningTag, DownloadTag, CommonDownloadTag,\
    InterimPreparationTag, CommonInterimPreparationTag, InitRamStartTag, CommonInitRamStartTag, NetworkTag,\
    CommonNetworkTag, StorageTag, CommonStorageTag, LateTestsTag, CommonLateTestsTag, PreparationTag,\
    CommonPreparationTag, RPMUpgradeTag, CommonRPMUpgradeTag, ApplicationsTag, CommonApplicationsTag,\
    ThirdPartyApplicationsTag, CommonThirdPartyApplicationsTag, FinalizationTag, CommonFinalizationTag,\
    FirstBootTag, CommonFirstBootTag, ReportTag, CommonReportTag


class IPUWorkflow(Workflow):
    name = 'InplaceUpgrade'
    tag = IPUTag
    short_name = 'ipu'
    description = '''No description has been provided for the InplaceUpgrade workflow.'''

    class FactsCollectionPhase(Phase):
        name = 'Facts collection'
        filter = Filter(TagFilter(IPUTag, phase=FactsTag),
                        TagFilter(phase=CommonFactsTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class ChecksPhase(Phase):
        name = 'Checks'
        filter = Filter(TagFilter(IPUTag, phase=ChecksTag),
                        TagFilter(phase=CommonChecksTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class ReportsPhase(Phase):
        name = 'Reports'
        filter = Filter(TagFilter(IPUTag, phase=ReportTag),
                        TagFilter(phase=CommonReportTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class AttachPackageReposPhase(Phase):
        name = 'AttachPackageRepos'
        filter = Filter(TagFilter(IPUTag, phase=AttachPackageReposTag),
                        TagFilter(phase=CommonAttachPackageReposTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class PlanningPhase(Phase):
        name = 'Planning'
        filter = Filter(TagFilter(IPUTag, phase=PlanningTag),
                        TagFilter(phase=CommonPlanningTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class DownloadPhase(Phase):
        name = 'Download'
        filter = Filter(TagFilter(IPUTag, phase=DownloadTag),
                        TagFilter(phase=CommonDownloadTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class InterimPreparationPhase(Phase):
        name = 'InterimPreparation'
        filter = Filter(TagFilter(IPUTag, phase=InterimPreparationTag),
                        TagFilter(phase=CommonInterimPreparationTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class InitRamStartPhase(Phase):
        name = 'InitRamStart'
        filter = Filter(TagFilter(IPUTag, phase=InitRamStartTag),
                        TagFilter(phase=CommonInitRamStartTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class NetworkPhase(Phase):
        name = 'Network'
        filter = Filter(TagFilter(IPUTag, phase=NetworkTag),
                        TagFilter(phase=CommonNetworkTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class StoragePhase(Phase):
        name = 'Storage'
        filter = Filter(TagFilter(IPUTag, phase=StorageTag),
                        TagFilter(phase=CommonStorageTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class LateTestsPhase(Phase):
        name = 'LateTests'
        filter = Filter(TagFilter(IPUTag, phase=LateTestsTag),
                        TagFilter(phase=CommonLateTestsTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class PreparationPhase(Phase):
        name = 'Preparation'
        filter = Filter(TagFilter(IPUTag, phase=PreparationTag),
                        TagFilter(phase=CommonPreparationTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class RPMUpgradePhase(Phase):
        name = 'RPMUpgrade'
        filter = Filter(TagFilter(IPUTag, phase=RPMUpgradeTag),
                        TagFilter(phase=CommonRPMUpgradeTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class ApplicationsPhase(Phase):
        name = 'Applications'
        filter = Filter(TagFilter(IPUTag, phase=ApplicationsTag),
                        TagFilter(phase=CommonApplicationsTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class ThirdPartyApplicationsPhase(Phase):
        name = 'ThirdPartyApplications'
        filter = Filter(TagFilter(IPUTag, phase=ThirdPartyApplicationsTag),
                        TagFilter(phase=CommonThirdPartyApplicationsTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class FinalizationPhase(Phase):
        name = 'Finalization'
        filter = Filter(TagFilter(IPUTag, phase=FinalizationTag),
                        TagFilter(phase=CommonFinalizationTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()

    class FirstBootPhase(Phase):
        name = 'FirstBoot'
        filter = Filter(TagFilter(IPUTag, phase=FirstBootTag),
                        TagFilter(phase=CommonFirstBootTag))
        policies = Policies(Policies.Errors.FailPhase,
                            Policies.Retry.Phase)
        flags = Flags()
