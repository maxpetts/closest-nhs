use reqwest::StatusCode;
use std::collections::HashMap;
use wasm_bindgen::prelude::*;
use web_sys::*;
use yew::*;

struct Model {}

#[function_component(App)]
fn app() -> Html {
    let mut organisations = HashMap::new();
    organisations.insert("GP", "GP");
    organisations.insert("Trust", "Trust");
    organisations.insert("Clinic", "Clinic");
    organisations.insert("Sustain", "Sustainability and Transformation Partnership");
    organisations.insert("Dentist", "Dentists");
    organisations.insert("Pharmacy", "Pharmacy");
    organisations.insert("AreaTeam", "Area Team");
    organisations.insert("CareHome", "Care homes and care at home");
    organisations.insert("Hospital", "Hospital");
    organisations.insert("MinorInj", "Minor Injury Unit");
    organisations.insert("LocalAuth", "Local Authority");
    organisations.insert("Opticians", "Opticians");
    organisations.insert("GenDirOfServ", "Generic Directory of Services");
    organisations.insert("HealthAuth", "Health Authority");
    organisations.insert("HealthWell", "Health and Wellbeing Board");
    organisations.insert("GPPractice", "GP practice");
    organisations.insert("UrgentCare", "Urgent Care");
    organisations.insert("SocialProv", "Social care provider");
    organisations.insert("StratHealth", "Strategic Health Authority");
    organisations.insert("RegionalArea", "Regional Area Team");
    organisations.insert("GenServDir", "Generic Service Directory");
    organisations.insert("ClinCommisGrp", "Clinical Commissioning Group");

    let org_type_ref = use_node_ref();
    let query_ref = use_node_ref();
    let result_ref = use_node_ref();

    let onclick = {
        let org_type_ref = org_type_ref.clone();
        let query_ref = query_ref.clone();
        let result_ref = result_ref.clone();

        wasm_bindgen_futures::spawn_local(async {
            async move {
                console::log_1(&"in move".into());
                let dropdown = &org_type_ref.cast::<web_sys::HtmlSelectElement>().unwrap();

                let selected = dropdown
                    .options()
                    .item(dropdown.selected_index().try_into().unwrap())
                    .unwrap()
                    .inner_html();

                match send_request().await {
                    Ok(res) => result_ref
                        .cast::<web_sys::HtmlElement>()
                        .unwrap()
                        .set_inner_text(format! {"{:#?}", res}.as_str()),
                    Err(err) => result_ref
                        .cast::<web_sys::HtmlElement>()
                        .unwrap()
                        .set_inner_text(format! {"Error fetching: {}", err}.as_str()),
                };
            };
        });
    };

    html! {
        <div>
            <h1>{"NHS Search"}</h1>
            <div>
                    <h3>{"Organisation type"}</h3>
                    <input ref={query_ref}/>
                    <select ref={org_type_ref}>
                        {organisations
                            .iter()
                            .map(|option| {
                                html! {
                                    <option>{&option.1}</option>
                                }
                            })
                            .collect::<Html>()}
                    </select>
            </div>
            <button >{"Search"}</button>
            <h1>{"Result:"}</h1>
            <p ref={result_ref}></p>
        </div>
    }
}

// async fn send_request() -> HashMap<String, String> {
async fn send_request() -> Result<HashMap<String, String>, &'static str> {
    let resp = reqwest::get("localhost:80").await.unwrap();

    match resp.status() {
        StatusCode::OK => {
            let resp = resp.json::<HashMap<String, String>>().await.unwrap();

            for val in resp.values() {
                console::log_1(&format!("resp: {}", val).into());
            }

            Ok(resp)
        }
        StatusCode::NOT_FOUND => {
            console::log_1(&"Cannot find server".into());
            Err("404")
        }
        _ => {
            console::log_1(&"/eh".into());
            Err("Unknown")
        }
    }
}

fn main() {
    yew::Renderer::<App>::new().render();
}
