from core.repair_tools.Nopol import Nopol


def run(args):
    bug = args.bug
    tool = Nopol(name="DynaMoth", seed=args.seed, statement_type=args.statement_type, synthesis="dynamoth")

    result = tool.repair(bug)
    pass


def dynamoth_args(parser):
    parser.set_defaults(func=run)
    parser.add_argument("--statement-type", "-t",
                        help="The targeted statement [condition, precondition, pre_then_cond]", default="pre_then_cond")
    parser.add_argument("--seed", "-s", help="The random seed", default=7)
    pass
