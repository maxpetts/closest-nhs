use yew::*;

struct SearchQuery {
    organisation: String,
    query: String,
}

enum Msg {
    Result,
    NoneFound,
    SelectChange,
}

enum Organisations {
    GP,
    Trust,
    Clinic,
    Sustain,
    Dentist,
    Pharmacy,
    AreaTeam,
    CareHome,
    Hospital,
    MinorInj,
    LocalAuth,
    Opticians,
    GenServDir,
    HealthAuth,
    HealthWell,
    GPPractice,
    UrgentCare,
    SocialProv,
    StratHealth,
    RegionalArea,
    GenDirOfServ,
    ClinCommisGrp,
}

struct MyComponent {
    organisation: String,
}

impl Component for MyComponent {
    type Message = Msg;
    type Properties = ();

    fn create(_: &yew::Context<Self>) -> Self {
        Self {
            organisation: String::new(),
        }
    }

    fn view(&self, ctx: &yew::Context<Self>) -> yew::virtual_dom::VNode {
        // let onclick = ctx.link().callback(|_| Msg::Search);

        let org_types = vec![
            Organisations::GP,
            Organisations::Trust,
            Organisations::Clinic,
            Organisations::Sustain,
            Organisations::Dentist,
            Organisations::Pharmacy,
            Organisations::AreaTeam,
            Organisations::CareHome,
            Organisations::Hospital,
            Organisations::MinorInj,
            Organisations::LocalAuth,
            Organisations::Opticians,
            Organisations::GenServDir,
            Organisations::HealthAuth,
            Organisations::HealthWell,
            Organisations::GPPractice,
            Organisations::UrgentCare,
            Organisations::SocialProv,
            Organisations::StratHealth,
            Organisations::RegionalArea,
            Organisations::GenDirOfServ,
            Organisations::ClinCommisGrp,
        ];

        let on_select_change = .callback(|e| {

        })
        html! {
            <div>
                <h1>{"NHS Search"}</h1>
                <div>
                    <h3>{"Organisation type"}</h3>
                    <select onchange={on_select_change}>
                        <option selected=false value="">{"GP"}</option>
                        {org_types.iter().map(|type| html!{
                            <option value=type>
                        })}
                    </select>
                </div>
                <button {onclick}>{"Search"}</button>
            </div>
        }
    }

    fn rendered(&mut self, ctx: &Context<Self>, first_render: bool) {
        // create link to server
    }

    fn update(&mut self, ctx: &Context<Self>, msg: Self::Message) -> bool {
        match msg {
            Msg::Result => true,
            Msg::NoneFound => true,
            _ => false,
        }
    }
}

fn main() {
    yew::start_app::<MyComponent>();
    let document = window().unwrap().document().unwrap();
    let mount_el = document.query_selector("#main").unwrap().unwrap();
}
